from cms.params.cms import cms_test_flow
from google.params.google import google_test_flow
from smartocto.params.notifications import notifications_test_flow
from smartocto.params.smartocto import smartocto_test_flow

from prefect.deployments import Deployment

cms = Deployment.build_from_flow(
    flow=cms_test_flow,
    name="dep-from-python",
    version=1, 
    work_queue_name="development",
    work_pool_name="default-agent-pool",
)

cms.apply()

google = Deployment.build_from_flow(
    flow=google_test_flow,
    name="dep-from-python",
    version=1, 
    work_queue_name="development",
    work_pool_name="default-agent-pool",
)

google.apply()

smartocto = Deployment.build_from_flow(
    flow=smartocto_test_flow,
    name="dep-from-python",
    version=1, 
    work_queue_name="development",
    work_pool_name="default-agent-pool",
)

smartocto.apply()

notifications = Deployment.build_from_flow(
    flow=notifications_test_flow,
    name="dep-from-python",
    version=1, 
    work_queue_name="development",
    work_pool_name="default-agent-pool",
)

notifications.apply()