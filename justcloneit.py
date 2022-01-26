# !/usr/bin/env python

import inkex


class JustCloneIt(inkex.EffectExtension):

  def thisworksright(self):
    # See Nup.generate_nup().make_clones
    ideal = inkex.Rectangle(x='50', y='50', width='10', height='10')
    layer = self.svg.add(inkex.Layer.new('Test Layer'))
    model = layer.add(ideal.copy())
    model.set('id', 'testmodel')
    use = layer.add(inkex.Use())
    use.set('xlink:href', '#' + 'testmodel')
    use.transform.add_translate(40, 40)

  def tmp(self):
    layername = 'bxm.' + datetime.datetime.now().replace(
      microsecond=0).isoformat()
    model = inkex.Rectangle(x='50', y='50', width='10', height='10')

    lyr = inkex.Layer.new('a')
    self.svg.add(lyr)

    ogn = inkex.Rectangle(x='50', y='50', width='10', height='10')
    ogn.set_id(modelname)
    lyr.add(ogn)

    ause = inkex.Use()
    # ause.transform.add_translate(20, 20)
    # r = inkex.Transform('translate(20, 20)')
    ause.transform.add_translate(20, 20)
    ause.set('xlink:href', modelname)
    lyr.add(ause)

    el1 = inkex.Rectangle(x='10', y='60', width='30', height='20')
    lyr.add(el1)


if __name__ == '__main__':
  JustCloneIt().run()
