from prefect import flow, task

@task(name="smartocto test")
def test_smartocto():
    smartocto = "Testing smartocto configuration"
    return smartocto
    
@task(name="passed smartocto test")
def passed_test(smartocto):
    print(smartocto)
    
@flow(name="smartocto flow")
def smartocto_test_flow():
    test = test_smartocto()
    passed_test(test)
    
if __name__ == "__main__":
    smartocto_test_flow()