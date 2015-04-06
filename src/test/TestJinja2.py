from jinja2 import Template
 
tmpl = Template(u'''\
<!DOCTYPE html>
<html>
  <head>
    <title>{{ title }}</title>
  </head>
  <body>
  {% for item in item_list -%}
    {{ item }}{% if not loop.last %}, !{% endif %}
  {%- endfor %}
  ------------------------------------------------
  {% for item in item_list -%}
    {{ item }}{% if not loop.last %}, !{% endif %}
  {% endfor %}
  ------------------------------------------------
  {{ item_list }}
  </body>
</html>
''')
  
print tmpl.render(
    title = 'Value with <unsafe> data',
    item_list = [1, 2, 3, 4, 5, 6]
)



# This produces the HTML:

# <!DOCTYPE html>
# <html>
#   <head>
#     <title>Value with <unsafe> data</title>
#   </head>
#   <body>
#   1, !2, !3, !4, !5, !6
#   ------------------------------------------------
#   1, !
#   2, !
#   3, !
#   4, !
#   5, !
#   6
#   
#   ------------------------------------------------
#   [1, 2, 3, 4, 5, 6]
#   </body>
# </html>



# str = ''
# for t in open('template.html').readlines():
#     str += t
# print repr(str)