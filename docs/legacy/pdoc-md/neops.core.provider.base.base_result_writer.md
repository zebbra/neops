# neops.core.provider.base.base_result_writer
## BaseResultWriter
Writes/updates the result object

----------

### Methods
```python
write_results(self,results: neops.core.provider.base.result.provider_result_composite.ProviderResultsComposite,execution_id: int,run_on_result: neops.core.provider.base.enum.RunOnEnum,success_message: str = '',subtask_finish: bool = False,task_finish: bool = False,neops_task_id: Union[int, NoneType] = None,granularity: int = 5) -> NoneType
```
This method is called on the beginning and the end of a task or a subtask (pre- and post run tasks).

It updates the result set in the databae for the relevant entities on which the task is executed and informs
the user over the progress.

\
__param__ results (ProviderResultsComposite): All results of the run cycle methods
\
__param__ execution_id (int): id of the current execution
\
__param__ run_on_result (RunOnEnum): for which entity the results should be stored
\
__param__ success_message (str, optional): message to be set for a successfully processed element
\
__param__ subtask_finish (bool, optional): identifies if a subtask (pre- or post run task is finished)
\
__param__ task_finish (bool, optional): identifies if the main task is finished
\
__param__ neops_task_id (Optional[int], optional): the id of the task whichone ran
\
__param__ granularity (int, optional): describes the importance of a task result
(values from 1-10, higher values are more important results, default is 5)

----------