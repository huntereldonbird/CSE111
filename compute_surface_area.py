import math

def main():
    names = ["#1 Picnic", "#1 Tall", "#2",	"#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short", "#10", "#211", "#300", "#303"]
    radius = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
    heights = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
    costs = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]

    max_value = -1
    max_name = ""

    for i in range(12):
        volume = compute_volume(radius[i], heights[i])
        surface_area = compute_surface_area(radius[i], heights[i])
        storage_efficiency = compute_storage_efficiency(volume, surface_area)
        cost = compute_cost_efficiency(volume, costs[i])
        print(f"{names[i]} {storage_efficiency:.2f} ${cost:.2f}")

        if cost < max_value:
            max_value = cost
            max_name = names[i]

    print(f"{max_name.capitalize()} has the best cost efficiency with {max_value:.2f}")

def compute_volume(radius, height):
    volume = math.pi * (radius * radius) * height
    return volume

def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(volume, surface_area):
    storage_efficiency = volume / surface_area
    return storage_efficiency

def compute_cost_efficiency(volume, cost):
    cost_efficiency = volume / cost
    return cost_efficiency

main()