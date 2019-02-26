import typing
import pandas as pd


class DataModel:

    def __init__(self, csv_path: str):

        self.df = pd.read_csv(csv_path)

    def bad_columns(self) -> typing.List[str]:
        return [col for col in self.df if self.df[self.df[col].isna()].shape[0]/self.df.shape[0] > 0.4]


class Controller:
    def __init__(self, model: DataModel):
        self.model = model

    def get_bad_cols(self):
        return self.model.bad_columns()


class View:

    def __init__(self, controller: Controller):
        self.controller = controller

    def list_bad_cols(self):
        cols = self.controller.get_bad_cols()
        for col in cols:
            print(f'Column \"{col}\" lacks too much data')


if __name__ == '__main__':

    model = DataModel('data/house_prices/train.csv')
    controller = Controller(model)
    view = View(controller)
    view.list_bad_cols()
