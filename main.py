import argparse
import matplotlib.pyplot as plt
import json

arg = argparse.ArgumentParser()
arg.add_argument("-d", "--data", help="Data file", required=False, default="data.json")
arg.add_argument("-x", "--x-label", help="X-Axis label", required=False, default="X-Axis")
arg.add_argument("-y", "--y-label", help="Y-Axis label", required=False, default="Y-Axis")
arg.add_argument("-o", "--output", help="Output file", required=False, default="output.png")
# add bar and line argument
arg.add_argument("-b", "--bar", help="bar chart", action="store_true")
arg.add_argument("-l", "--line", help="line chart", action="store_true")

args = arg.parse_args()

if args.bar and args.line:
    print("You can't use both bar and line chart")
    exit()
elif args.bar and args.line == False:
    print("You need to choose one of the chart type")
    exit()
elif args.bar:
    dictionary = json.load(open(args.data, 'r'))
    xAxis = [key for key, value in dictionary.items()]
    yAxis = [value for key, value in dictionary.items()]
    plt.grid(True)

    plt.plot(xAxis,yAxis, color='maroon', marker='o')
    plt.xlabel(args.x_label)
    plt.ylabel(args.y_label)

    plt.show()
elif args.line:
    dictionary = json.load(open(args.data, 'r'))
    xAxis = [key for key, value in dictionary.items()]
    yAxis = [value for key, value in dictionary.items()]
    plt.grid(False)

    fig = plt.figure()
    plt.bar(xAxis,yAxis, color='maroon')
    plt.xlabel(args.x_label)
    plt.ylabel(args.y_label)

    plt.show()