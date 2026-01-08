# Default arguments
def deploy(env="dev"):
    print(f"Deploying to {env} environment")

deploy()          # o/p: Deploying to dev environment
deploy("prod")    # o/p: Deploying to prod environment


# Keyword arguments
def create_user(username, role="user"):
    print(f"Creating user: {username} with role: {role}")   

create_user(role="admin", username="ekta")
# o/p: Creating user: ekta with role: admin