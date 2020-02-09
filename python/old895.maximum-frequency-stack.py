#
# @lc app=leetcode id=895 lang=python3
#
# [895] Maximum Frequency Stack
#
# https://leetcode.com/problems/maximum-frequency-stack/description/
#
# algorithms
# Hard (57.90%)
# Total Accepted:    19.7K
# Total Submissions: 34K
# Testcase Example:  '["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"]\n' +
#  '[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]'
#
# Implement FreqStack, a class which simulates the operation of a stack-like
# data structure.
# 
# FreqStack has two functions:
# 
# 
# push(int x), which pushes an integer x onto the stack.
# pop(), which removes and returns the most frequent element in the
# stack.
# 
# If there is a tie for most frequent element, the element closest to the top
# of the stack is removed and returned.
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: 
# 
# ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
# [[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
# Output: [null,null,null,null,null,null,null,5,7,5,4]
# Explanation:
# After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to
# top.  Then:
# 
# pop() -> returns 5, as 5 is the most frequent.
# The stack becomes [5,7,5,7,4].
# 
# pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the
# top.
# The stack becomes [5,7,5,4].
# 
# pop() -> returns 5.
# The stack becomes [5,7,4].
# 
# pop() -> returns 4.
# The stack becomes [5,7].
# 
# 
# 
# 
# Note:
# 
# 
# Calls to FreqStack.push(int x) will be such that 0 <= x <= 10^9.
# It is guaranteed that FreqStack.pop() won't be called if the stack has zero
# elements.
# The total number of FreqStack.push calls will not exceed 10000 in a single
# test case.
# The total number of FreqStack.pop calls will not exceed 10000 in a single
# test case.
# The total number of FreqStack.push and FreqStack.pop calls will not exceed
# 150000 across all test cases.
# 
# 
# 
# 
# 
# 
#
from collections import OrderedDict, Counter, defaultdict
from itertools import count
class OrderedCounter(Counter, OrderedDict):
     'Counter that remembers the order elements are first encountered'

     def __repr__(self):
         return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

     def __reduce__(self):
         return self.__class__, (OrderedDict(self),)


class FreqStack:

    def __init__(self):
        self.d = OrderedCounter()
        self.c = count()
        self.added = defaultdict(list)
    def push(self, x: int) -> None:
        if not self.d:
            self.d[x] = 1
            self.added[x].append(next(self.c))
            # print('x=', x, self.d)
            # print('added=', self.added)
        else:
            if x not in self.d:
                self.d[x] = 1
                self.added[x].append(next(self.c))
                # print('x=', x, self.d)
                # print('added=', self.added)
            else:
                self.d[x] += 1
                self.added[x].append(next(self.c))
                # self.added[x] = next(self.c)

                # equal_keys = [k for k,v in self.d.items() if v == self.d[x] and k != x]
                # print(equal_keys, self.added)
                # if equal_keys:
                    # self.added[x] = next(self.c)

                # print('x=', x, self.d)
                # print('added=', self.added)
    
    def pop(self) -> int:
        mc = self.d.most_common()
        if not mc:
            return None

        fmc = list(filter(lambda x: x[1] ==  mc[0][1], mc))
        # print(fmc)
        if len(fmc) == 1:
            k, v = fmc[0]
            self.d[k] = v - 1
            self.added[k].pop()
            if self.d[k] == 0:
                del self.d[k]
                del self.added[k]
            # print(self.d)
            # print(self.added)
            return k
        else:
            # print('here', fmc)
            # print(fmc)
            # print(self.added)

            # print([self.added[k] for k,v in fmc])
            # print([self.added[k][-1] for k,v in fmc])
            # print(max([self.added[k][-1] for k,v in fmc]))
            # print([k for k,v in self.added.items() if v[-1] == max(self.added[k][-1] for k,v in fmc)])

            k = [k for k,v in self.added.items() if v[-1] == max(self.added[k][-1] for k,v in fmc)][0]
            v = self.d[k]
            self.d[k] = v - 1
            self.added[k].pop()
            if self.d[k] == 0:
                del self.d[k]
                del self.added[k]
            # print(self.d)
            # print(self.added)
            return k
            # print(k)

            
# Your FreqStack object will be instantiated and called as such:
obj = FreqStack()
# obj.push(5)
# obj.push(7)
# obj.push(5)
# obj.push(7)
# obj.push(4)
# obj.push(5)
# print(obj.pop() == 5)
# print(obj.pop() == 7)
# print(obj.pop() == 5)
# print(obj.pop() == 4)

# obj.push(1)
# obj.push(0)
# obj.push(0)
# obj.push(1)
# obj.push(5)
# obj.push(4)
# obj.push(1)
# obj.push(5)
# obj.push(1)
# obj.push(6)

# print(obj.pop() == 1)
# print(obj.pop() == 1)
# print(obj.pop() == 5)
# print(obj.pop() == 1)
# print(obj.pop() == 0)
# print(obj.pop() == 6)
# print(obj.pop() == 4)
# print(obj.pop() == 5)
# print(obj.pop() == 0)
# print(obj.pop() == 1)



command = ["FreqStack","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","push","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop"]
params = [[],[442],[309],[364],[908],[997],[319],[267],[269],[784],[909],[193],[104],[333],[831],[848],[951],[420],[43],[45],[807],[375],[170],[282],[100],[917],[430],[505],[200],[523],[253],[940],[866],[719],[564],[731],[84],[362],[882],[791],[315],[384],[139],[0],[951],[184],[801],[178],[455],[544],[185],[281],[139],[3],[368],[840],[220],[433],[393],[515],[214],[47],[330],[980],[580],[452],[294],[717],[148],[614],[500],[68],[501],[338],[10],[449],[204],[106],[687],[554],[391],[705],[877],[365],[526],[891],[266],[452],[486],[360],[561],[788],[872],[413],[283],[768],[704],[274],[443],[247],[524],[208],[70],[264],[87],[299],[328],[310],[930],[764],[261],[905],[482],[15],[469],[84],[275],[961],[532],[985],[442],[333],[229],[247],[772],[591],[861],[480],[871],[901],[74],[668],[74],[353],[127],[633],[124],[88],[736],[678],[846],[909],[713],[829],[288],[458],[545],[398],[462],[482],[517],[38],[148],[772],[866],[207],[112],[234],[879],[443],[980],[496],[116],[765],[119],[696],[997],[745],[814],[426],[62],[225],[859],[789],[574],[202],[478],[819],[109],[903],[78],[722],[18],[855],[315],[551],[43],[667],[998],[302],[838],[151],[36],[667],[271],[715],[65],[133],[316],[519],[240],[126],[111],[366],[62],[542],[29],[520],[317],[39],[22],[582],[712],[180],[571],[85],[466],[817],[189],[465],[904],[268],[783],[77],[274],[777],[868],[291],[411],[331],[192],[329],[839],[574],[844],[571],[677],[555],[212],[491],[344],[229],[316],[920],[963],[968],[545],[275],[365],[296],[963],[864],[788],[520],[485],[736],[890],[717],[948],[603],[839],[607],[550],[822],[447],[844],[257],[975],[732],[195],[684],[289],[97],[132],[433],[949],[237],[543],[440],[170],[695],[304],[45],[850],[762],[46],[452],[319],[656],[313],[700],[45],[908],[647],[398],[818],[741],[313],[89],[639],[424],[868],[150],[831],[844],[205],[255],[614],[284],[487],[533],[393],[123],[284],[811],[800],[101],[693],[880],[611],[961],[589],[468],[401],[584],[661],[993],[149],[325],[894],[686],[308],[563],[62],[150],[38],[846],[136],[372],[329],[697],[73],[9],[172],[568],[354],[76],[286],[265],[727],[714],[20],[835],[106],[400],[424],[29],[107],[742],[688],[789],[969],[889],[301],[657],[660],[227],[760],[910],[591],[782],[281],[845],[331],[304],[564],[612],[466],[832],[755],[525],[884],[401],[389],[981],[314],[133],[855],[689],[321],[807],[678],[453],[530],[950],[540],[104],[439],[304],[959],[437],[400],[766],[766],[79],[680],[934],[581],[277],[933],[64],[490],[198],[555],[401],[882],[72],[465],[288],[109],[845],[649],[352],[532],[447],[59],[330],[33],[99],[850],[782],[296],[17],[882],[67],[244],[849],[574],[439],[781],[919],[577],[922],[68],[520],[687],[847],[476],[629],[289],[730],[579],[990],[528],[192],[793],[451],[131],[963],[495],[168],[201],[254],[927],[813],[34],[701],[328],[438],[743],[293],[292],[931],[788],[832],[743],[960],[755],[746],[291],[705],[937],[571],[718],[175],[465],[529],[730],[519],[236],[986],[484],[118],[841],[366],[952],[30],[762],[680],[716],[36],[504],[],[504],[],[299],[],[88],[],[613],[],[366],[],[986],[],[234],[],[391],[],[659],[],[134],[],[150],[],[88],[],[848],[],[786],[],[118],[],[281],[],[663],[],[58],[],[60],[],[189],[],[777],[],[248],[],[747],[],[163],[],[634],[],[675],[],[639],[],[174],[],[465],[],[252],[],[323],[],[332],[],[910],[],[186],[],[395],[],[782],[],[79],[],[778],[],[905],[],[620],[],[926],[],[455],[],[779],[],[997],[],[495],[],[453],[],[953],[],[696],[],[504],[],[396],[],[717],[],[973],[],[504],[],[464],[],[507],[],[40],[],[824],[],[724],[],[628],[],[698],[],[809],[],[433],[],[572],[],[241],[],[557],[],[651],[],[563],[],[195],[],[278],[],[39],[],[420],[],[578],[],[353],[],[669],[],[384],[],[470],[],[201],[],[532],[],[216],[],[221],[],[429],[],[637],[],[515],[],[228],[],[571],[],[703],[],[212],[],[120],[],[868],[],[342],[],[561],[],[488],[],[512],[],[314],[],[151],[],[699],[],[679],[],[937],[],[498],[],[851],[],[503],[],[988],[],[167],[],[300],[],[770],[],[422],[],[563],[],[887],[],[213],[],[65],[],[17],[],[619],[],[946],[],[239],[],[505],[],[428],[],[493],[],[824],[],[886],[],[585],[],[473],[],[908],[],[443],[],[303],[],[478],[],[662],[],[234],[],[745],[],[374],[],[60],[],[698],[],[885],[],[910],[],[982],[],[47],[],[974],[],[901],[],[891],[],[7],[],[671],[],[197],[],[901],[],[275],[],[57],[],[587],[],[693],[],[533],[],[412],[],[68],[],[724],[],[8],[],[579],[],[97],[],[455],[],[582],[],[246],[],[755],[],[256],[],[866],[],[393],[],[687],[],[451],[],[320],[],[92],[],[612],[],[51],[],[468],[],[406],[],[292],[],[251],[],[487],[],[882],[],[794],[],[307],[],[595],[],[631],[],[723],[],[625],[],[63],[],[143],[],[789],[],[262],[],[568],[],[53],[],[581],[],[288],[],[41],[],[14],[],[238],[],[516],[],[753],[],[30],[],[507],[],[335],[],[607],[],[702],[],[84],[],[247],[],[869],[],[664],[],[167],[],[538],[],[364],[],[154],[],[406],[],[530],[],[657],[],[883],[],[274],[],[989],[],[368],[],[648],[],[395],[],[449],[],[687],[],[742],[],[68],[],[22],[],[347],[],[317],[],[446],[],[946],[],[301],[],[227],[],[431],[],[333],[],[412],[],[526],[],[113],[],[757],[],[633],[],[754],[],[440],[],[175],[],[743],[],[873],[],[892],[],[722],[],[125],[],[293],[],[691],[],[40],[],[283],[],[387],[],[797],[],[27],[],[274],[],[637],[],[4],[],[309],[],[736],[],[465],[],[743],[],[245],[],[714],[],[156],[],[629],[],[790],[],[62],[],[281],[],[331],[],[884],[],[69],[],[411],[],[996],[],[92],[],[956],[],[72],[],[543],[],[449],[],[684],[],[286],[],[472],[],[867],[],[162],[],[896],[],[95],[],[174],[],[224],[],[538],[],[310],[],[470],[],[59],[],[301],[],[5],[],[122],[],[658],[],[557],[],[462],[],[25],[],[759],[],[98],[],[699],[],[407],[],[873],[],[97],[],[351],[],[41],[],[938],[],[616],[],[339],[],[161],[],[891],[],[355],[],[125],[],[469],[],[363],[],[819],[],[60],[],[767],[],[889],[],[60],[],[680],[],[726],[],[758],[],[869],[],[467],[],[647],[],[587],[],[441],[],[133],[],[543],[],[527],[],[345],[],[730],[],[887],[],[509],[],[379],[],[509],[],[738],[],[301],[],[825],[],[661],[],[703],[],[595],[],[67],[],[647],[],[867],[],[669],[],[842],[],[145],[],[455],[],[718],[],[947],[],[83],[],[205],[],[239],[],[254],[],[648],[],[410],[],[924],[],[675],[],[696],[],[907],[],[861],[],[28],[],[424],[],[650],[],[724],[],[904],[],[205],[],[496],[],[900],[],[186],[],[42],[],[424],[],[174],[],[33],[],[394],[],[635],[],[645],[],[857],[],[281],[],[276],[],[904],[],[55],[],[596],[],[136],[],[759],[],[116],[],[837],[],[291],[],[932],[],[632],[],[771],[],[203],[],[672],[],[657],[],[400],[],[555],[],[537],[],[842],[],[998],[],[820],[],[498],[],[101],[],[632],[],[973],[],[215],[],[134],[],[190],[],[89],[],[512],[],[201],[],[886],[],[892],[],[872],[],[533],[],[448],[],[667],[],[406],[],[564],[],[62],[],[549],[],[560],[],[217],[],[180],[],[437],[],[901],[],[994],[],[709],[],[328],[],[329],[],[926],[],[266],[],[598],[],[722],[],[282],[],[927],[],[250],[],[992],[],[706],[],[528],[],[577],[],[893],[],[858],[],[43],[],[318],[],[9],[],[422],[],[706],[],[389],[],[563],[],[163],[],[205],[],[332],[],[255],[],[713],[],[780],[],[309],[],[838],[],[351],[],[833],[],[702],[],[500],[],[769],[],[789],[],[220],[],[899],[],[342],[],[62],[],[992],[],[993],[],[663],[],[43],[],[12],[],[782],[],[692],[],[842],[],[960],[],[627],[],[813],[],[366],[],[406],[],[617],[],[308],[],[655],[],[883],[],[448],[],[890],[],[764],[],[261],[],[67],[],[316],[],[596],[],[581],[],[162],[],[685],[],[318],[],[384],[],[112],[],[710],[],[249],[],[203],[],[896],[],[333],[],[808],[],[58],[],[504],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]


for c in range(len(command)):
    if command[c] == 'push':
        obj.push(params[c][0])
    elif command[c] == 'pop':
        print(obj.pop())

