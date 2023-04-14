# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 16:47:43 2023

@author: julia
"""

 <py-config>
                    packages = [
                      "https://cdn.holoviz.org/panel/0.14.3/dist/wheels/bokeh-2.4.3-py3-none-any.whl",
                      "numpy",
                    "ipywidgets",
                      "pandas",
                      "panel==0.13.1"
                    ]
                    plugins = [
                      "https://pyscript.net/latest/plugins/python/py_tutor.py"
                    ]
            
    <section class="pyscript">
         <h1>Bokeh Example</h1>
    <div id="myplot"></div>           
</py-config>


 <py-script id="main">                
                
from ipywidgets import Layout
import IPython.display as display
import ipywidgets as widgets
from ipywidgets import Layout, Box, VBox, HBox
from io import StringIO
import sys


city1=widgets.Combobox(
    placeholder='City 1:',
    options=['Atlanta','Boston','Calgary','Charleston','Chicago','Dallas','Denver','Duluth','El Paso','Helena',
'Houston','Kansas City','Las Vegas','Little Rock','Los Angeles','Miami',
'Montreal', 'Nashville','New Orleans','New York','Oklahoma City','Omaha','Phoenix','Pittsburgh','Portland',
'Raleigh','Saint Louis','Salt Lake City','San Francisco','Santa Fe','Seattle','Sault St. Marie','Toronto','Vancouver','Washington','Winnipeg'],
    description='Choose:',
    ensure_option=True,
    disabled=False
)
city2=widgets.Combobox(
    
    placeholder='City 2:',
    options=['Atlanta','Boston','Calgary','Charleston','Chicago','Dallas','Denver','Duluth','El Paso','Helena',
'Houston','Kansas City','Las Vegas','Little Rock','Los Angeles','Miami',
'Montreal', 'Nashville','New Orleans','New York','Oklahoma City','Omaha','Phoenix','Pittsburgh','Portland',
'Raleigh','Saint Louis','Salt Lake City','San Francisco','Santa Fe','Seattle','Sault St. Marie','Toronto','Vancouver','Washington','Winnipeg'],
    description='Choose:',
    ensure_option=True,
    disabled=False
)


city3=widgets.Combobox(
    placeholder='City 3:',
    value=None,
    options=['Atlanta','Boston','Calgary','Charleston','Chicago','Dallas','Denver','Duluth','El Paso','Helena',
'Houston','Kansas City','Las Vegas','Little Rock','Los Angeles','Miami',
'Montreal', 'Nashville','New Orleans','New York','Oklahoma City','Omaha','Phoenix','Pittsburgh','Portland',
'Raleigh','Saint Louis','Salt Lake City','San Francisco','Santa Fe','Seattle','Sault St. Marie','Toronto','Vancouver','Washington','Winnipeg'],
    description='Choose:',
    ensure_option=True,
    disabled=False
)

city4=widgets.Combobox(
    placeholder='City 4:',
    value=None,
    options=['Atlanta','Boston','Calgary','Charleston','Chicago','Dallas','Denver','Duluth','El Paso','Helena',
'Houston','Kansas City','Las Vegas','Little Rock','Los Angeles','Miami',
'Montreal', 'Nashville','New Orleans','New York','Oklahoma City','Omaha','Phoenix','Pittsburgh','Portland',
'Raleigh','Saint Louis','Salt Lake City','San Francisco','Santa Fe','Seattle','Sault St. Marie','Toronto','Vancouver','Washington','Winnipeg'],
    description='Choose:',
    ensure_option=True,
    disabled=False
)

city5=widgets.Combobox(
    placeholder='City 5:',
    value=None,
    options=['Atlanta','Boston','Calgary','Charleston','Chicago','Dallas','Denver','Duluth','El Paso','Helena',
'Houston','Kansas City','Las Vegas','Little Rock','Los Angeles','Miami',
'Montreal', 'Nashville','New Orleans','New York','Oklahoma City','Omaha','Phoenix','Pittsburgh','Portland',
'Raleigh','Saint Louis','Salt Lake City','San Francisco','Santa Fe','Seattle','Sault St. Marie','Toronto','Vancouver','Washington','Winnipeg'],
    description='Choose:',
    ensure_option=True,
    disabled=False
)


city6=widgets.Combobox(
    placeholder='City 6:',
    value=None,
    options=['Atlanta','Boston','Calgary','Charleston','Chicago','Dallas','Denver','Duluth','El Paso','Helena',
'Houston','Kansas City','Las Vegas','Little Rock','Los Angeles','Miami',
'Montreal', 'Nashville','New Orleans','New York','Oklahoma City','Omaha','Phoenix','Pittsburgh','Portland',
'Raleigh','Saint Louis','Salt Lake City','San Francisco','Santa Fe','Seattle','Sault St. Marie','Toronto','Vancouver','Washington','Winnipeg'],
    description='Choose:',
    ensure_option=True,
    disabled=False
)


print("hi")
