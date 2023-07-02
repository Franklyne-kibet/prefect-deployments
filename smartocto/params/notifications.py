from prefect import flow, task

@task(name="notification test")
def test_notifications():
    notifications = "Testing notifications configuration"
    return notifications
    
@task(name="passed notifications test")
def passed_test(notifications):
    print(notifications)
    
@flow(name="notifications flow")
def notifications_test_flow():
    test = test_notifications()
    passed_test(test)
    
if __name__ == "__main__":
    notifications_test_flow()