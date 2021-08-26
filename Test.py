import pandas as pd
import os
import IndeedScraper
import LinkedInScaper

r1 = IndeedScraper.scrape("software engineer intern", "united kingdom")
r2 = LinkedInScaper.scrape("software engineer intern")

r1[0] += r2[0]
r1[1] += r2[1]
r1[2] += r2[2]
r1[3] += r2[3]

data = pd.DataFrame({
    'Title': r1[0], 
    'Company': r1[1], 
    'Location': r1[2], 
    'Links': r1[3]
})

data['Links'] = '<a target="_blank" href=' + data['Links'] + '>Click Here</a>'
pd.set_option('colheader_justify', 'center')

html_string = '''
    <html>
        <head><title>Software Engineering Internships</title></head>
        <link rel="stylesheet" type="text/css" href="df_style.css"/>
        <body>
            <h1>Software Engineer Internships</h1>
            {table}
        </body>
    </html>.
    '''

with open('WebPage.html', 'w') as f:
    f.write(html_string.format(table=data.to_html(classes='mystyle', escape=False)))

print("Written successfully.")
os.system("start WebPage.html")