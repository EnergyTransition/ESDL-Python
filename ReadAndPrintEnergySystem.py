from model import esdl_sup as esdl

def load_energy_system(inpath):
    with open(inpath, 'r') as infile:
        # parse esdl file
        es = esdl.parse(infile, silence=True)
        return es


def iterate_over_building(bld, level):
    sub_assets = bld.get_asset()

    for sub_asset in sub_assets:
        for i in range(level):
            print(" ", end='')
        print("Asset " + sub_asset.get_name())
        if isinstance(sub_asset, esdl.AggregatedBuilding) or isinstance(sub_asset, esdl.Building) \
                or isinstance(sub_asset, esdl.BuildingUnit):
            iterate_over_building(sub_asset, level+2)


def iterate_over_area(area, level):
    sub_assets = area.get_asset()
    sub_areas = area.get_area()

    for sub_area in sub_areas:
        for i in range(level):
            print(" ", end='')
        print("Area "+sub_area.get_name())
        iterate_over_area(sub_area)

    for sub_asset in sub_assets:
        for i in range(level):
            print (" ", end='')
        print("Asset " + sub_asset.get_name())
        if isinstance(sub_asset, esdl.AggregatedBuilding) or isinstance(sub_asset, esdl.Building) \
                or isinstance(sub_asset, esdl.BuildingUnit):
            iterate_over_building(sub_asset, level+2)


if __name__ == "__main__":

    es = load_energy_system('test.esdl')
    # get all assets of an area within the energy system (use 1st instance only)
    area = es.get_instance()[0].get_area()

    print("Area " + area.get_name())
    iterate_over_area(area, 2)