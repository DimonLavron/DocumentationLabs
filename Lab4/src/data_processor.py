from urllib.request import urlopen
import json

def validate_data(data):
    if data is dict:
        data = [data]
    fields = ['incident_key', 'occur_date', 'occur_time', 'boro', 'precinct', 'jurisdiction_code', 'location_desc', 'statistical_murder_flag',
        'perp_age_group', 'perp_sex', 'perp_race', 'vic_age_group', 'vic_sex', 'vic_race', 'x_coord_cd', 'y_coord_cd', 'latitude', 'longitude']
    for entry in data:
        entry['precinct'] = int(entry['precinct'])
        entry['jurisdiction_code'] = int(entry['jurisdiction_code'])
        entry['statistical_murder_flag'] = int(entry['statistical_murder_flag'])
        entry['x_coord_cd'] = int(entry['x_coord_cd'])
        entry['y_coord_cd'] = int(entry['y_coord_cd'])
        entry['latitude'] = int(float(entry['latitude']))
        entry['longitude'] = int(float(entry['longitude']))

        for field in fields:
            if entry.get(field) is None:
                entry[field] = ''

class Writer:
    def __init__(self, resource_name, url_template, data_handler_strategy, logger_strategy,
                 step=100, offset=0, limit=None):
        self.resource_name = resource_name
        self.paginator = Paginator(
            url_template=url_template, step=step, offset=offset, limit=limit)
        self.data_handler = data_handler_strategy()
        self.logger = logger_strategy()

    def process_data(self):
        log_status = self.logger.get_status(self.resource_name)
        if log_status == 'COMPLETED':
            self.logger.log_already_exists(self.resource_name)
            return
        elif log_status == 'START':
            self.paginator.offset = self.logger.get_logged_rows_number(self.resource_name)
        else:
            self.logger.log_start(self.resource_name)

        for data in self.paginator:
            data_range = [
                self.paginator.offset - self.paginator.step + 1,
                min(self.paginator.offset,
                    self.paginator.offset - (self.paginator.step - len(data))
                    )]
            self.data_handler.process_data(data)
            self.logger.log_progress(self.resource_name, data_range=data_range)
        self.logger.log_completed(self.resource_name)


class Paginator:
    def __init__(self, url_template, step=100, offset=0, limit=None):
        self.url_template = url_template
        self.step = step
        self.offset = offset
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.limit and self.offset >= self.limit:
            raise StopIteration
        result = self.query_data()
        if result:
            return result
        raise StopIteration

    def query_data(self):
        result = None
        with urlopen(self.url_template.format(
                step=self.step, offset=self.offset
        )) as data:
            result = json.loads(data.read().decode('utf-8'))
            validate_data(result)
            self.offset += self.step

        return result
