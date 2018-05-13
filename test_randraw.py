from randdraw import RandDraw

def test_draw_will_not_repeat_drawn_elements():
    # given
    l = ['cow','goat','sheep']
    rd = RandDraw(l[:])

    # when
    firstDraw = rd.draw()
    secondDraw = rd.draw()
    thirdDraw = rd.draw()

    # then
    assert firstDraw != secondDraw
    assert firstDraw != thirdDraw
    assert secondDraw != thirdDraw

def test_reset_will_allow_you_to_start_over():
    # given
    l = ['a','b']
    rd = RandDraw(l[:])
    rd.draw()

    # when
    rd.reset()
    firstRedraw = rd.draw()
    secondRedraw = rd.draw()
    
    # then
    assert firstRedraw in l and secondRedraw in l
    assert rd.done()

def test_done_should_correctly_indicate_when_all_elements_drawn():
    # given
    l = ['cow','goat','sheep']
    rd = RandDraw(l[:])

    # when
    for i in range(0,len(l)):
        rd.draw()
    
    # then
    assert rd.done()

def test_done_should_correctly_indicate_when_elements_remain():
    # given
    l = ['cow','goat','sheep']
    rd = RandDraw(l[:])

    # when
    rd.draw() # draw once
    
    # then
    assert not rd.done()