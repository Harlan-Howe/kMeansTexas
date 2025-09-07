import random

import pyglet
from pyglet import shapes
from typing import Tuple, List
from ZipCodeItemFile import ZipcodeItem

Coordinates = Tuple[float, float]
GROUP_COLORS = ((192,0,0),(0,192,0),(0,0,192),(192,192,0),(192,0,192),(0,192,192), (255,128, 0), (128,128,128),
                (255,128,128), (128,255,0))  # feel free to add more colors!

class Display(pyglet.window.Window):
    """
    Essentially, the window, but this also is what is holding the list of attractor positions.
    """
    def __init__(self, k:int):

        super(Display,self).__init__(791,713,"Zip Codes")

        self.texas_image = pyglet.image.load('texas56.png')
        self.spr = None

        self.city_coords = None
        self.city_group_numbers = None
        self.city_colors = None
        self.vector_list = None
        self.background_group = pyglet.graphics.Group(0)
        self.foreground_group = pyglet.graphics.Group(1)
        self.previous_attractor_group = pyglet.graphics.Group(2)
        self.star_outline_group = pyglet.graphics.Group(3)
        self.current_star_group = pyglet.graphics.Group(4)
        self.circles_list = []
        self.stars_list = []
        self.previous_attractors = []
        self.current_attractors = []
        self.N = k

    def on_draw(self) -> None:
        """
        This is what should happen every second or so.
        :return: None
        """
        self.clear()
        self.batch.draw()

    def set_cities(self, zip_code_item_list: List[ZipcodeItem]) -> None:
        """
        this display keeps track of the cities it needs to plot on top of the graphic; this receives the list of
        zipcodeitems and stores all the coordinates.
        :param zip_code_item_list: - a list of zipcodeItems that we will want to plot.
        :return: None
        """
        self.city_coords = []
        self.city_group_numbers = []
        self.city_colors = []
        for zip in zip_code_item_list:
            self.city_coords.append((int(zip.x),int(zip.y)))
            self.city_group_numbers.append(zip.attractor_number)
            self.city_colors.append(GROUP_COLORS[self.city_group_numbers[-1]])
        self.batch = self.build_batch()

    def build_batch(self) -> pyglet.graphics.Batch:
        """
        This is essentially where the drawing stuff happens - this is generating the list of instructions of what to
        do every time the computer refreshes the window... which may happen at a different rate than our code is
        changing what we want to see.
        :return: the "Batch" set of things to draw.
        """
        # print("building batch.")
        batch = pyglet.graphics.Batch()

        # draw the texas map
        self.spr = pyglet.sprite.Sprite(self.texas_image, x=0, y=0, batch=batch, group=self.background_group)

        # draw all the dots
        self.circles_list = []

        for i in range(len(self.city_colors)):
            self.circles_list.append(shapes.Circle(x=self.city_coords[i][0],
                                   y=self.city_coords[i][1],
                                   radius=2,
                                   color = self.city_colors[i],
                                   batch=batch,
                                   group = self.foreground_group))

        # OK. Time to draw stars....
        self.star_list = []
        # first, draw the trail of old stars, if any.
        """
        # Draws previous stars along the path (optional)
        for j in range(len(self.previous_attractors)):
            i = j % self.N
            self.star_list.append(shapes.Star(x=self.previous_attractors[j][0],
                                              y=self.previous_attractors[j][1],
                                              outer_radius=20,
                                              inner_radius=2,
                                              num_spikes=5,
                                              color=GROUP_COLORS[i],
                                              batch=batch,
                                              group=self.previous_attractor_group
                                              ))
        """
        # Draws lines between the previous stops along the attractor's path
        for j in range(self.N, len(self.previous_attractors)):
            i = j % self.N
            self.star_list.append(shapes.Line(x = self.previous_attractors[j-self.N][0],
                                              y = self.previous_attractors[j-self.N][1],
                                              x2 = self.previous_attractors[j][0],
                                              y2 = self.previous_attractors[j][1],
                                              thickness = 2,
                                              color = GROUP_COLORS[i],
                                              batch = batch,
                                              group = self.previous_attractor_group
                                              ))
        # connects the last of the previous attractors to the current location of each attractor with a line
        if len(self.previous_attractors) > 0:
            for i in range(self.N):
                self.star_list.append(shapes.Line(x = self.previous_attractors[-1-i][0],
                                                  y = self.previous_attractors[-1-i][1],
                                                  x2= self.current_attractors[-1-i][0],
                                                  y2= self.current_attractors[-1-i][1],
                                                  thickness = 2,
                                                  color = GROUP_COLORS[self.N-1-i],
                                                  batch = batch,
                                                  group = self.previous_attractor_group
                                                  ))
        # Now draw the current stars -- first the black outlines, then the fills.
        for i in range(self.N):
            #outline
            self.star_list.append(shapes.Star(x=self.current_attractors[i][0],
                                              y=self.current_attractors[i][1],
                                              outer_radius=8,
                                              inner_radius=5,
                                              num_spikes=5,
                                              rotation=90,
                                              color=(0, 0, 0),
                                              batch=batch,
                                              group=self.star_outline_group,
                                              ))
            # color fill
            self.star_list.append(shapes.Star(x=self.current_attractors[i][0],
                                              y=self.current_attractors[i][1],
                                              outer_radius=5,
                                              inner_radius=2,
                                              num_spikes=5,
                                              rotation=90,
                                              color=GROUP_COLORS[i],
                                              batch=batch,
                                              group=self.current_star_group,
                                              ))
        return batch

    def update_city_colors(self, zip_code_items:List[ZipcodeItem]) -> None:
        """
        the colors of the cities now need to change - this tells the batch to update, so they show up correctly next
        time the window refreshes.
        :param zip_code_items: the list of zipcodeitems, which contains the attractor numbers.
        :return:  None
        """
        for i in range(len(self.city_group_numbers)):
            self.city_colors[i] = GROUP_COLORS[zip_code_items[i].attractor_number]
        self.batch = self.build_batch()

    def update_attractor_locations(self, attractor_locations: List[Coordinates]) -> None:
        """
        updates the current locations of the attractors, and keeps a record of the previous locations, so we can draw
        the trail...
        :param attractor_locations: the k coordinates of the attractors now.
        :return: None
        """
        if attractor_locations is None or len(attractor_locations) == 0:
            return
        self.previous_attractors.extend(self.current_attractors)
        self.current_attractors = attractor_locations

