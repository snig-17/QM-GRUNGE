import requests
import uuid
from bs4 import BeautifulSoup
from typing import Any, Dict


def request_expedition_data(expedition_code: str) -> Dict[str, Any]:
    request_id = str(uuid.uuid4())
    url = "https://www.himalayandatabase.com/scripts/getexprecrdmc.php"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,"
                "image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Cache-Control": "max-age=0",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://www.himalayandatabase.com",
        "Referer": "https://www.himalayandatabase.com/scripts/getexplist.php",
        "Sec-Ch-Ua": '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"macOS"',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
    }
    cookies = {
        "request_id": request_id
    }
    data = {
        "ExpList": expedition_code
    }
    response = requests.post(url, headers=headers, cookies=cookies, data=data, timeout=30)


    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    mbr_list_select = soup.find("select", id="MbrList")

    member_count = None

    if mbr_list_select:
        fieldset = mbr_list_select.find_parent("fieldset")
        if fieldset:
            legend = fieldset.find("legend")
            if legend:
                text = legend.get_text(strip=True)
                parts = text.split("Member Count =")
                if len(parts) == 2:
                    member_count = int(parts[1].strip())

    def find_from_input_tag(soup, input_id):
        input_tag = soup.find("input", id=input_id)
        if input_tag and input_tag.has_attr("value"):
            return input_tag["value"].strip()
        return None

    total_members = find_from_input_tag(soup, "TotMbrs")
    death_mbrs = find_from_input_tag(soup, "DthMbrs")
    hired_deaths = find_from_input_tag(soup, "DthHired")
    return {
        "member_count": member_count,
        "total_members": total_members,
        "death_mbrs": death_mbrs,
        "hired_deaths": hired_deaths
    }
