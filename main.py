import random
from typing import List, Tuple
from datetime import datetime
import pyglet
import csv
from DisplayFile import Display
from ZipCodeItemFile import ZipcodeItem

k = 5


def start_display() -> None:
    """
    creates the window that will show the graphic. Sets it to update every 1.0 seconds.
    :return:
    """
    global dsp, steps
    steps = 0
    dsp = Display(k)
    load_data()
    initialize_stars()
    dsp.set_cities(zip_list)


    pyglet.clock.schedule_interval(do_update,1.0)
    pyglet.app.run()


def load_data() -> None:
    """
    Loads the zip code data from a file. Creates the global "zip_list" - a list of ZipCodeItems.
    :return:
    """
    global zip_list  # the list of cities, represented as a list of ZipCodeItem instances.
    tsv_file = open("Texas zips with coordinates.tsv")
    read_tsv = csv.reader(tsv_file, delimiter="\t")
    zip_list = []
    for zipcode in read_tsv:
        zci = ZipcodeItem(zipcode[0],zipcode[1],zipcode[2],int(zipcode[5]),713-int(zipcode[4])) # we skip 3 because it is the name of the city, which we don't need.
        zci.attractor_number = random.randrange(k)
        zip_list.append(zci)


def initialize_stars() -> None:
    """
    picks k independent zip code items from our zip_list at random and uses them for our stars' starting points.
    :return: None
    """
    indices = []
    locs = []
    for i in range(k):
        index = random.randrange(len(zip_list))
        while index in indices:
            index = random.randrange(len(zip_list))
        indices.append(index)
        locs.append((zip_list[index].x,zip_list[index].y))
    dsp.update_attractor_locations(locs) # update the graphics about where the stars are.


def do_update(dt: float) -> None:
    """
    Performs the two steps of the k-Means algorithm and checks whether to continue or not.
    This method is getting called automatically every second, per line 23, so it represents a single cycle of the
    algorithm.
    :param dt: the time since the last time do_update() was called. (Unused in this program.)
    :return: None
    """
    global steps
    print(f"{steps}")
    did_update = True  # We're going to check whether anything changed by the end of this method. Change this, if needed.

    # TODO #3: write the code that will do one cycle of the two steps of this algorithm, updating the attractors for
    #          each city and the locations of each attractor.

    # To update the cities, you will need to update the "attractor_number" for each item in the zip_list, and then call
    dsp.update_city_colors(zip_list)

    # To update the attractor locations, you will need to make a new list of attractors' locations:
    attractors: List[Tuple[int,int]] = []
    # ... and add the new location of each attractor to it.

    # Then call
    dsp.update_attractor_locations(attractors)

    steps += 1
    if not did_update:
        pyglet.clock.unschedule(do_update)  # stop the animation.
        print("No More Changes.")
        pyglet.image.get_buffer_manager().get_color_buffer().save(
            f"resulting images/Texas {k=}-{datetime.now().strftime(
                '%b %d %H-%M-%S')}.png")


if __name__ == "__main__":
    start_display()