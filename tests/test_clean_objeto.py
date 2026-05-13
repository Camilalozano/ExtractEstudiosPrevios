import unittest

from extractor_estudios_previos import clean_objeto_text


class CleanObjetoTextTests(unittest.TestCase):
    def test_removes_inline_atenea_footer_from_objeto(self):
        text = (
            "Prestar servicios profesionales para apoyar la gestión contractual. "
            "Cualquier copia impresa de este documento se considera como COPIA NO CONTROLADA. "
            "LOS DATOS PROPORCIONADOS SERÁN TRATADOS DE ACUERDO CON LA LEY 1581 DE 2012 "
            "Y LA POLÍTICA DE TRATAMIENTO DE DATOS PERSONALES DE LA AGENCIA PUBLICADA EN "
            "LA PÁGINA WEB https://agenciaatenea.gov.co/ VERSIÓN:4 09/12/2025"
        )

        self.assertEqual(
            clean_objeto_text(text),
            "Prestar servicios profesionales para apoyar la gestión contractual",
        )


if __name__ == "__main__":
    unittest.main()
