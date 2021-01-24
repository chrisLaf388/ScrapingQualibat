popo = 'elena est en vacaces'
position = popo.find('z')
if popo.startswith('vaca', position):

    print(len(popo))
    positionless = len(popo) - position
    print(popo[:-positionless])


else:
    print('no')