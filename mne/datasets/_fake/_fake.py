# Authors: Alexandre Gramfort <alexandre.gramfort@telecom-paristech.fr>
#          Martin Luessi <mluessi@nmr.mgh.harvard.edu>
#          Eric Larson <larson.eric.d@gmail.com>
# License: BSD Style.

from ...utils import verbose
from ..utils import (_data_path, _data_path_doc,
                     _get_version, _version_doc)


@verbose
def data_path(path=None, force_update=False, update_path=False,
              download=True, verbose=None):
    return _data_path(path=path, force_update=force_update,
                      update_path=update_path, name='fake',
                      download=download)

data_path.__doc__ = _data_path_doc.format(name='fake',
                                          conf='MNE_DATASETS_FAKE_PATH')


def get_version():
    return _get_version('fake')

get_version.__doc__ = _version_doc.format(name='fake')
