class BaseDeployer:
    def deploy(self):
        print("Checking config")

class AppDeployer(BaseDeployer):
    def deploy(self):
        super().deploy()  # Call method from BaseDeployer
        print("Deploying application")

a = AppDeployer() # python looks for deploy method in AppDeployer first, then in BaseDeployer
a.deploy()

# Output:
# Checking config
# Deploying application