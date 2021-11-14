import os, json

from github import Github #pygithub https://github.com/PyGithub/PyGithubpip
import git # gitpython https://gitpython.readthedocs.io/
import requests



gh_pa_token = os.getenv("PA_TOKEN", default=None)

g = Github(gh_pa_token)


def main():
    
    for repo in g.get_user().get_repos():
        print(repo.name)
    
    repositoriy_search= g.search_repositories(query="language:python")
    for repo in repositoriy_search:
        print(repo)

    #Get repositories for an organization
    org = g.get_organization('abacchi')
    repos = org.get_repos()
    repos_id_lsit=[]
    for repo in repos:
        repos_id_lsit.append(repo.id)
    print(repos_id_lsit)



def function_example(param1: int, param2: str) -> bool:
    """ example text to explain the function
    Args:
        param1: first parameter which is an int
        param2: second parameter which is a str
        
    Returns:
        the return value. its true for success, false otherwise
        
    """



if __name__ == "__main__":
    main()