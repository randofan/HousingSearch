# Housing Search
## Cloning Repository
1. Clone the repository
2. Ensure that python3 is installed. Check via `python3 --version`
3. Open the python virtual environment from command line. \
Windows: `./env/Scripts/activate` \
Unix: `source env/Scripts/activate`
4. Run `python3 app.py`
5. Open `localhost`

## Using HousingSearch API
```
from utils import Filters, House
from housingsearch import search_all

filters = Filters(price=2000, baths=2, beds=4)
houses: list[House] = search_all(filters)
# sort by price
houses.sort(key=lambda house:house.price)
```
The list of housing results are temporarily cached for a day before a query is made again. This is to prevent 
making too many requests, so the IP address isn't banned from Craigslist or Zillow.

# React Instruction
### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.