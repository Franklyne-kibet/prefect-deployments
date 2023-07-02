from prefect import flow, task

@task(name="cms")
def test_cms():
    cms = "Testing CMS configuration"
    return cms
    
@task(name="cms task")
def passed_test(cms):
    print(cms)
    
@flow(name="cms flow")
def cms_test_flow():
    test = test_cms()
    passed_test(test)
    
if __name__ == "__main__":
    cms_test_flow()