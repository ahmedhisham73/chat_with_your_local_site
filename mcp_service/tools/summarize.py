import requests
from bs4 import BeautifulSoup

def summarize_page(url: str) -> dict:
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        text = " ".join(p.text for p in paragraphs[:5])
        return {"summary": text[:500] + "..."}
    except Exception as e:
        return {"summary": f"Error: {str(e)}"}