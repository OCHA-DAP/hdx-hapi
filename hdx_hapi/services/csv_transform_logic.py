import csv
import io

from typing import Dict, List, Type

from fastapi.responses import StreamingResponse
from hdx_hapi.endpoints.models.base import HapiBaseModel

from hdx_hapi.endpoints.util.util import OutputFormat


MAX_ITEMS_IN_BATCH = 5000


def transform_result_to_csv_stream_if_requested(
        result: List[Dict], 
        output_format: OutputFormat, 
        pydantic_class: Type[HapiBaseModel]
    ) -> List[Dict] | StreamingResponse:
    """
    Transforms the result to a CSV stream if requested. Otherwise, returns the result as is
    """

    if output_format == OutputFormat.CSV:
        if result:
            def iter_csv(): 
                pydantic_instance = pydantic_class.model_validate(result[0])
                keys = pydantic_instance.list_of_fields()
                items_per_row = len(keys)
                header_row_generated = False
                i = 0
                while i < len(result):
                    total_items_in_batch = 0
                    with io.StringIO() as str_as_file:
                        writer = csv.writer(str_as_file)
                        if not header_row_generated:
                            writer.writerow(keys)
                            header_row_generated = True
                        while i < len(result):
                            item = result[i]
                            pydantic_model = pydantic_class.model_validate(item)
                            new_row = [getattr(pydantic_model, key, '') for key in keys]
                            writer.writerow(new_row)
                            i += 1
                            total_items_in_batch += items_per_row
                            if total_items_in_batch >= MAX_ITEMS_IN_BATCH:
                                break

                        csv_row = str_as_file.getvalue()
                        yield csv_row          

            response = StreamingResponse(iter_csv(), media_type='text/csv')
            response.headers['Content-Disposition'] = 'attachment; filename=results.csv'
            return response

        return StreamingResponse(iter([]), media_type='text/csv')
    return {'data': result}

