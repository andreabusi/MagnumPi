import rq
from rq.registry import StartedJobRegistry


class TasksHelpers:
    def __init__(self, queue_name, connection):
        self.registry = StartedJobRegistry(queue_name, connection=connection)
        self.queue_name = queue_name
        self.connection = connection

    def get_task_progress(self, job_id):
        try:
            rq_job = rq.job.Job.fetch(job_id, connection=self.connection)
        except ():
            rq_job = None
        return rq_job.meta.get('progress', 0) if rq_job is not None else 0

    def get_running_jobs(self):
        running_jobs = []
        for job_id in self.registry.get_job_ids():
            progress = self.get_task_progress(job_id)
            running_jobs.append({'job_id': job_id, 'progress': progress})
        return running_jobs

    def get_expired_jobs(self):
        return self.registry.get_expired_job_ids()

