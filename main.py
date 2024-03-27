from pyscript import document
import yake


def yake_extract(event):
    input_text = document.querySelector("#english")
    english = input_text.value
    output_div = document.querySelector("#output")
    kw_extractor = yake.KeywordExtractor()
    keywords = kw_extractor.extract_keywords(english)
    output_div.innerText = keywords