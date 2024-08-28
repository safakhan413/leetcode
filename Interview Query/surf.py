import requests
from bs4 import BeautifulSoup
import csv
import time

def search_jobs(query):
    url = f"https://www.indeed.com/jobs?q={query.replace(' ', '+')}&fromage=1"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = []

    # Find all divs with the specific class that contains job listings
    for div in soup.find_all('div', class_='cardOutline'):
        a = div.find('a', href=True)
        if a:
            title = a.text.strip()
            link = 'https://www.indeed.com' + a['href']
            jobs.append((title, link))
    
    return jobs

def main():
    queries = [
        "Python Developer",
        "Data Engineer",
        "Python Data Engineer",
        "Python Software Engineer"
    ]
    
    all_jobs = []
    
    for query in queries:
        print(f"Searching for {query}...")
        jobs = search_jobs(query)
        all_jobs.extend(jobs)
        time.sleep(2)  # Be polite, don't overwhelm the server
    
    # Write to CSV
    with open('job_listings.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Job Title', 'Link'])
        for job in all_jobs:
            writer.writerow([job[0], f'=HYPERLINK("{job[1]}", "{job[1]}")'])
    
    print(f"Done! {len(all_jobs)} jobs written to job_listings.csv")

if __name__ == "__main__":
    main()
