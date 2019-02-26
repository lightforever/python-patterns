import typing
import pandas as pd


class DataModel:

    def __init__(self, csv_path: str):

        self.df = pd.read_csv(csv_path)

    def bad_columns(self) -> typing.List[str]:
        return [col for col in self.df if self.df[self.df[col].isna()].shape[0]/self.df.shape[0] > 0.4]


class View:

    def list_bad_cols(self, cols: typing.List[str]):
        for col in cols:
            print(f'Column \"{col}\" lacks too much data')


class Controller:
    def __init__(self, model: DataModel, view: View):
        self.model = model
        self.view = view

    def get_bad_cols(self):
        cols = self.model.bad_columns()
        self.view.list_bad_cols(cols)



if __name__ == '__main__':

    model = DataModel('data/house_prices/train.csv')
    controller = Controller(model)
    view = View(controller)
    view.list_bad_cols()
