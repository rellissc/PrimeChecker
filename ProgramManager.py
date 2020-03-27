from GUIManager import PrimeCheckerApp
import PrimeChecker

file='galleryJSON.json'
currentData=PrimeChecker.ReadJSONFile(file)
MyWindow = PrimeCheckerApp(currentData, 'Test')