from eve import Eve

# initialise Eve application
app = Eve()

# run the app when the program is executed as a main program
if __name__ == '__main__':
    app.run(debug=True)