import re
from pathlib import Path

from playwright.sync_api import expect, sync_playwright


# Responsável: Pedro Vital


def test_filtrar_restaurantes_da_categoria_italiana():
    """TF01: filtra a categoria Italiana e confere os restaurantes exibidos."""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        try:
            context = browser.new_context(viewport={"width": 1440, "height": 1000})
            try:
                page = context.new_page()
                page.add_init_script('localStorage.setItem("userId", "1"); localStorage.setItem("userName", "Pedro Vital");')
                page.goto("https://local-eats-unisenac.vercel.app/", wait_until="domcontentloaded")

                expect(page).to_have_title("Local Eats | Descubra a Gastronomia Local")
                page.locator(".rest-card").first.wait_for(state="visible", timeout=30_000)

                filtro_italiana = page.get_by_role("button", name="Italiana", exact=True)
                filtro_italiana.click()
                expect(filtro_italiana).to_have_class(re.compile(r"\bactive\b"))

                restaurantes = page.locator(".rest-card")
                expect(restaurantes.first).to_be_visible(timeout=30_000)
                assert restaurantes.count() > 0
                cozinhas_exibidas = restaurantes.locator(".card-meta").all_inner_texts()
                assert all("Italiana" in cozinha for cozinha in cozinhas_exibidas)

                evidencia = Path(__file__).parents[1] / "evidencias" / "filtro-categoria-italiana.png"
                evidencia.parent.mkdir(parents=True, exist_ok=True)
                page.screenshot(path=str(evidencia), full_page=True)
            finally:
                context.close()
        finally:
            browser.close()

