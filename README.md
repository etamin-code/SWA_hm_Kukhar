# SWA_hm_Kukhar

you can run nodes manually or using run_nodes.sh:
bash run_nodes.sh

## task 3

After map initializing
![photo_2022-06-01_22-35-21](https://user-images.githubusercontent.com/70692373/171487556-364f0ea2-572f-4a04-8735-45bdd387c41c.jpg)

After deleting one node


![photo_2022-06-01_22-39-57](https://user-images.githubusercontent.com/70692373/171488083-9ea0e77e-d274-4216-916a-54b4e0c986c2.jpg)

After deleting second node

![Screenshot from 2022-06-01 22-42-44](https://user-images.githubusercontent.com/70692373/171491043-e5efa408-e507-4746-89fc-388fc8b3fac2.png)

So, as we can see - all the data is saved.

But if delete two nodes at once, we may to lose the data:
![Screenshot from 2022-06-01 22-45-41](https://user-images.githubusercontent.com/70692373/171491070-f7a855c6-d743-446a-b726-641fd8fd57f9.png)

## task 4

without locking, value=1237 (must be 3000)

![Screenshot from 2022-06-01 22-54-52](https://user-images.githubusercontent.com/70692373/171491088-8eff68de-ee27-4d0c-9050-24bc343f5262.png)

with pessimistic locking works

![Screenshot from 2022-06-01 23-03-41](https://user-images.githubusercontent.com/70692373/171491694-996ebc59-9cba-4670-95b1-c57b3a42ffb1.png)

with optimistic locking works

![Screenshot from 2022-06-01 23-06-27](https://user-images.githubusercontent.com/70692373/171492123-0d42dc53-9c57-4e5e-a5e3-28967de2abfc.png)

## task 5
If nobody reads the queue, writer stops after queue become filled.
If there is 2 ot more readers, they read faster then writer write the data, so some part of time readers have te wait on new data.
