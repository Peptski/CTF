function controlCar(scanArray) {

	switch(Math.max([scanArray[0], scanArray[4], scanArray[8], scanArray[12], scanArray[16]])) {
    case scanArray[0]: return -1
	case scanArray[4]: return -1
    case scanArray[8]: return 0
    case scanArray[12]: return 1
    case scanArray[16]: return 1
	}

}