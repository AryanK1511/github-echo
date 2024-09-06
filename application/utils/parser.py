def parse_github_url(github_repository_url):
    url_split_arr = github_repository_url.split("/")
    return url_split_arr[3], url_split_arr[4]
