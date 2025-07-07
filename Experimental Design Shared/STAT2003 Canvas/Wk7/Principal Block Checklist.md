## ✅ PRINCIPAL BLOCK CHECKLIST

> 🧰 Use this method whenever you’re assigning treatments to blocks in confounded factorial designs (e.g. 242^424, 252^525, etc.)

---

### 🔷 **Step 1: List Defining Contrasts**

- Write down the **confounded effects** (generators), e.g.:
    

I=ABC,I=ACDI = ABC,\quad I = ACDI=ABC,I=ACD

---

### 🔷 **Step 2: List All Treatment Combinations**

- Use standard notation:  
    (1),a,b,ab,c,ac,bc,abc,d,ad,bd,abd,cd,acd,bcd,abcd(1), a, b, ab, c, ac, bc, abc, d, ad, bd, abd, cd, acd, bcd, abcd(1),a,b,ab,c,ac,bc,abc,d,ad,bd,abd,cd,acd,bcd,abcd
    

---

### 🔷 **Step 3: For Each Treatment:**

For **each defining contrast**:

1. Count how many **letters it shares** with the contrast
    
2. If it shares an **even number of letters** → score a ✓
    
3. It must satisfy this **for all defining contrasts** to be included in Block 1
    

---

### 🔷 **Step 4: Collect the Treatments with ✓✓✓…**

- Those treatments go into **Block 1** (principal block)
    
- Once Block 1 is set, generate the rest by multiplication
    

---

### 📋 Example – Use Case:

You’re working with 242^424, and want 4 blocks using:

I=ABC,ACDI = ABC,\quad ACDI=ABC,ACD

|Treatment|Shared with ABC|Even?|Shared with ACD|Even?|Block 1?|
|---|---|---|---|---|---|
|(1)|0|✅|0|✅|✅|
|a|1 (A)|❌|1 (A)|❌|❌|
|ac|2 (A, C)|✅|2 (A, C)|✅|✅|
|bcd|2 (B, C)|✅|2 (C, D)|✅|✅|
|abd|2 (A, B)|✅|2 (A, D)|✅|✅|
|abc|3 (A,B,C)|❌|2 (A,C)|✅|❌|
|abcd|4 (A,B,C,D)|✅|3 (A,C,D)|❌|❌|

✔️ Block 1 = { (1), ac, bcd, abd }

---

## 🧠 Exam Tip:

> If you're stuck, just remember:  
> 🔹 Even number of common letters with **every** confounded effect = principal block  
> 🔹 Use multiplication (mod-2 logic) to generate other blocks