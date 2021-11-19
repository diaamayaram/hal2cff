from hal2cff import hal2cff
import ipywidgets as widgets
from IPython.display import display, display_html, Markdown

# # hal2cff example


# +
query = widgets.Textarea(value='https://hal.archives-ouvertes.fr/hal-01361430v1')
button = widgets.Button(description="Print CFF")
display(widgets.HBox([query, button]))
output = widgets.Output()
display(output)

def run_and_display_query(_):
    with output:
        output.clear_output()
        #display_html(hal2cff(query.value))
        display(print(hal2cff(query.value)))
        

button.on_click(run_and_display_query)
# -

print(hal2cff("https://hal.archives-ouvertes.fr/hal-01361430v1"))


