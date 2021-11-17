import os, json

from github import Github #pygithub https://github.com/PyGithub/PyGithub
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


def create_issue(g: str, repo_name: str, title: str, body: str):
    """creates new issues in the specified repo
    Args:
        g: the github auth info to create the issue
        repo_name: full repo name ex: ORG/Seeker_scanner
        title: title of issue
        body: body text of issue
    """

    repo = g.get_repo(repo_name)
    repo.create_issue(title=title, body=body)

def review_git_issues(repo_name: str):
    """pulls up the existing issues in a repo
    Args:
        repo_name: full repo name ex: ORG/Seeker_scanner
    """
    issues_array = []
    repo = g.get_repo(repo_name)
    open_issues = repo.get_issues(state="open")
    for oi in open_issues:
        issues_array.append(oi.title)

def git_clone(cloneurl: str):
    """this clones a github repo
    Args:
        cloneurl: the git clone url for the repo
    """

    repo= git.Repo.clone_from(cloneurl, ".", depth=1) #depth is shallow


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