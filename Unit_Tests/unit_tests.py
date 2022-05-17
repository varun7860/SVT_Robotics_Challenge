import sys
import math
import pkg_resources

def check_version()->bool:
    assert(sys.version_info.major == 3)

def check_installations()->bool:
    required = {'numpy','math','requests'}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    built_in = set(sys.builtin_module_names)
    missing = required - installed - built_in
    assert(len(missing)==0)

def test_distance_function(x1=2,x2=3,y1=7,y2=10,ans = 3.16)->bool:
    assert(round(math.sqrt(pow(x2-x1,2) + pow(y2-y1,2)),2)==ans)
   
def main():
    check_version()
    check_installations()
    test_distance_function()

if __name__ == '__main__':
    main()
