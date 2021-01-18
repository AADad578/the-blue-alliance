import grpc
from .base import CloudTasksTransport
from google.api_core import gapic_v1
from google.auth import credentials
from google.cloud.tasks_v2.types import cloudtasks, queue, queue as gct_queue, task, task as gct_task
from google.iam.v1 import iam_policy_pb2 as iam_policy, policy_pb2 as policy
from google.protobuf import empty_pb2 as empty
from typing import Any, Callable, Optional, Sequence, Tuple

class CloudTasksGrpcTransport(CloudTasksTransport):
    def __init__(self, *, host: str=..., credentials: credentials.Credentials=..., credentials_file: str=..., scopes: Sequence[str]=..., channel: grpc.Channel=..., api_mtls_endpoint: str=..., client_cert_source: Callable[[], Tuple[bytes, bytes]]=..., ssl_channel_credentials: grpc.ChannelCredentials=..., quota_project_id: Optional[str]=..., client_info: gapic_v1.client_info.ClientInfo=...) -> None: ...
    @classmethod
    def create_channel(cls: Any, host: str=..., credentials: credentials.Credentials=..., credentials_file: str=..., scopes: Optional[Sequence[str]]=..., quota_project_id: Optional[str]=..., **kwargs: Any) -> grpc.Channel: ...
    @property
    def grpc_channel(self) -> grpc.Channel: ...
    @property
    def list_queues(self) -> Callable[[cloudtasks.ListQueuesRequest], cloudtasks.ListQueuesResponse]: ...
    @property
    def get_queue(self) -> Callable[[cloudtasks.GetQueueRequest], queue.Queue]: ...
    @property
    def create_queue(self) -> Callable[[cloudtasks.CreateQueueRequest], gct_queue.Queue]: ...
    @property
    def update_queue(self) -> Callable[[cloudtasks.UpdateQueueRequest], gct_queue.Queue]: ...
    @property
    def delete_queue(self) -> Callable[[cloudtasks.DeleteQueueRequest], empty.Empty]: ...
    @property
    def purge_queue(self) -> Callable[[cloudtasks.PurgeQueueRequest], queue.Queue]: ...
    @property
    def pause_queue(self) -> Callable[[cloudtasks.PauseQueueRequest], queue.Queue]: ...
    @property
    def resume_queue(self) -> Callable[[cloudtasks.ResumeQueueRequest], queue.Queue]: ...
    @property
    def get_iam_policy(self) -> Callable[[iam_policy.GetIamPolicyRequest], policy.Policy]: ...
    @property
    def set_iam_policy(self) -> Callable[[iam_policy.SetIamPolicyRequest], policy.Policy]: ...
    @property
    def test_iam_permissions(self) -> Callable[[iam_policy.TestIamPermissionsRequest], iam_policy.TestIamPermissionsResponse]: ...
    @property
    def list_tasks(self) -> Callable[[cloudtasks.ListTasksRequest], cloudtasks.ListTasksResponse]: ...
    @property
    def get_task(self) -> Callable[[cloudtasks.GetTaskRequest], task.Task]: ...
    @property
    def create_task(self) -> Callable[[cloudtasks.CreateTaskRequest], gct_task.Task]: ...
    @property
    def delete_task(self) -> Callable[[cloudtasks.DeleteTaskRequest], empty.Empty]: ...
    @property
    def run_task(self) -> Callable[[cloudtasks.RunTaskRequest], task.Task]: ...
