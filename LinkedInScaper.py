from bs4 import BeautifulSoup
import requests

def scrape(title):
    
    output = []

    titles = []
    companys = []
    locations = []
    links = []

    count = 0

    title = title.replace(' ', '%20')

    url = "https://uk.linkedin.com/jobs/search?keywords=" + title + "&location=United%20Kingdom&locationId=&geoId=101165590&sortBy=DD&f_TPR=&position=1&pageNum=0"
    print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("ul", class_="jobs-search__results-list")

    jobs = results.find_all("div", class_="base-search-card__info")

    for link in results.select('a[class*="base-card__full-link"]'):
        links.append(link.get("href"))

    for job in jobs:

        title = job.find("h3", class_="base-search-card__title")

        if job.find("a", class_="hidden-nested-link"):
            company = job.find("a", class_="hidden-nested-link")
        else: company = job.find("div", class_="hidden-nest-link")

        location = job.find("span", class_="job-search-card__location")

        titles.append(title.text.strip())
        companys.append(company.text.strip())
        locations.append(location.text.strip())

        count += 1

    output = [titles, companys, locations, links]
    
    return output