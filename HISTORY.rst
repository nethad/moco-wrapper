=======
History
=======

0.4.0 (2020-02-19)
------------------

* Finished reworking all the integration tests
* Prefixed Employment, Holiday and Presense with "User" for clarification
* Moved duplicated methods id_generator and create_random date into base class
* Implented additional requestor that only tries once to request the api endpoint (no retrying)
* Main moco object moved to namespace moco_wrapper.moco
* Changed author email


0.3.0 (2020-02-17) 
------------------

* Create github workflow to automaticly deploy to PyPI
* Implement an objector to control how the json responses get converted back into python objects (some endpoints return data that contain reserved python keywords, this was implemented to circumvent that)
* More Tests and more type hinting
* Write the history of the last versions
* Change the order of things in this history file
* Implement offer creation

0.2.3 (2020-02-09)
------------------

* Implement FileResponses for downloading pdf files from api
* Implement invoice class api changes
* More tests

0.2.2 (2020-01-12)
------------------

* Start implementing type hinting
* Switch to support python3 only
* Remove company delete method, as it is not support by the api
* More Tests

0.2.1 (2020-01-10)
------------------

* More tests

0.1.0 (2019-09-04)
------------------

* First release on PyPI.







