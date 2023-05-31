import tkinter as tk
from secugen import getFP
from matcher import matchFP

countA = 0
countB = 0

def process_vote():
    aadhar = aadhar_entry.get()
    getFP(aadhar, 'secure_vote')
    score = matchFP(aadhar, 'secure_vote.bmp')
    
    if score > 6:
        selected_party = party_var.get()
        if selected_party == 1:
            global countA
            countA += 1
        else:
            global countB
            countB += 1
            
    aadhar_entry.delete(0, tk.END)
    party_var.set(0)
    
def end_voting():
    if countA > countB:
        result_label.config(text="Party A won.")
    else:
        result_label.config(text="Party B won.")

root = tk.Tk()
root.title("Secure Voting")

aadhar_label = tk.Label(root, text="Enter Aadhar Number:")
aadhar_label.pack()

aadhar_entry = tk.Entry(root)
aadhar_entry.pack()

party_label = tk.Label(root, text="Select Party:")
party_label.pack()

party_var = tk.IntVar()
partyA_radio = tk.Radiobutton(root, text="Party A", variable=party_var, value=1)
partyA_radio.pack()

partyB_radio = tk.Radiobutton(root, text="Party B", variable=party_var, value=2)
partyB_radio.pack()

partyC_radio = tk.Radiobutton(root, text="Party C", variable=party_var, value=3)
partyC_radio.pack()

partyD_radio = tk.Radiobutton(root, text="Party D", variable=party_var, value=4)
partyD_radio.pack()

vote_button = tk.Button(root, text="Vote", command=process_vote)
vote_button.pack()

end_button = tk.Button(root, text="End Voting", command=end_voting)
end_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()