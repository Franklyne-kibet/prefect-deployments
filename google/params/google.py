from prefect import flow, task

@task(name="google test")
def test_google():
    google = "Testing google configuration"
    return google
    
@task(name="passed google")
def passed_test(google):
    print(google)
    
@flow(name="google flow")
def google_test_flow():
    test = test_google()
    passed_test(test)
    
if __name__ == "__main__":
    google_test_flow()