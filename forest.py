import utilities
import turtle

#  Call the functions in the utilities module
utilities.setup_page()
utilities.draw_innersquare()
utilities.draw_circle(0,370,10, 0, 'green')
utilities.write_text(30,370,'Tree')
utilities.draw_circle(100,370,10, 0, 'white')
utilities.write_text(130,370,'Bird')

turtle.done()