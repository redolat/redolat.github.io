import os

md_files = [f.split(".")[0] for f in os.listdir() if f.endswith('.md')]
print(md_files)

description_dict = {
    "solid": "SOLID Programming",
    "tdd": "TDD Programming",
    "prefix": "Considering Comment Prefix",
    "pipeline": "Creating Pipelines",
    "client": "Client Satisfaction",
    "clear": "Clear Code",
    "wtp": "WTP (Willingness To Pay)",
    "github": "GitHub Manual",
    "db": "DataBase",
    "docker": "Docker",
    "environment": "Environment",
    "config": "Config",
    "postgres": "Postgres",
}

with open("index.md", 'w') as f:
    for md_file in md_files:
        f.write(f'<a href="/{md_file}.html">{description_dict.get(md_file, md_file.capitalize())}</a>\n<br>\n')
