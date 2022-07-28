import model_sum as model
import view

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    model.init(value_a, value_b)
    result = model.do_it()
    view.view_data(result, 'sum')

def new_button_clic():
    value_sens = view.get_sensor()
    model.write_it(value_sens)
    