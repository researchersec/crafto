import bs4

# Path to the HTML file (replace with your actual file path if needed)
html_file_path = 'engi250.html'

# Read the HTML content from the file
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML using BeautifulSoup
soup = bs4.BeautifulSoup(html_content, 'html.parser')

# Find all <a> tags and extract href attributes that match the pattern
matching_urls = []
for anchor in soup.find_all('a'):
    href = anchor.get('href')
    if href and href.startswith('https://www.wowhead.com/tbc/spell='):
        matching_urls.append(href)

# Remove duplicates by converting to a set and back to list (optional, but useful)
matching_urls = list(set(matching_urls))

# Print the matching URLs
print("Found matching URLs:")
for url in matching_urls:
    print(url)

# Optionally, save to a file
with open('extracted_urls.txt', 'a', encoding='utf-8') as output_file:
    for url in matching_urls:
        output_file.write(url + '\n')

print(f"\nTotal URLs found: {len(matching_urls)}")
print("URLs saved to 'extracted_urls.txt'")