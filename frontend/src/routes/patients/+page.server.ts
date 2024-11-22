export const load = async()=> {
    const getPatients = async()=>{
        const resp = await fetch('http://127.0.0.1:8000/api/patient',{headers: {Authorization:'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImU0NzIzYjJmLTEyYTktNGVkNi1iYzVmLWU3M2Y5N2E0MTZhOSIsImVtYWlsIjoidW1pQGV4YW1wbGUuY29tIiwiZXhwIjoxNzMyMjM5MDI0fQ.eRYqt4Vow_DjtGM1QXm2I3FC7L5oRBDvmdxLwYAY4ZQ','Content-Type': 'application/json'}})
        const data =await resp.json()
        return data
    }
    return {
        patients:await getPatients(),
    }
}

 
export const actions = {
    updatePatient: async ({ request }) => {
        const data = await request.formData();
        const formEntries = Object.fromEntries(data.entries()); 
        let patient ={
            name: data.get("name"),
            status: parseInt(data.get("status")),
            sex: parseInt(data.get("gender")),
            birth_date: data.get("birthdate").split("/").reverse().join("-"),
            cpf: data.get("cpf")
        }
        console.log(patient); 
        let id = data.get("id")
        async function editPatient(patient) {
            const response2 = fetch(`http://127.0.0.1:8000/api/patient/${id}`,{
            method: 'PUT',
            headers: {Authorization:'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImU0NzIzYjJmLTEyYTktNGVkNi1iYzVmLWU3M2Y5N2E0MTZhOSIsImVtYWlsIjoidW1pQGV4YW1wbGUuY29tIiwiZXhwIjoxNzMyMjM5MDI0fQ.eRYqt4Vow_DjtGM1QXm2I3FC7L5oRBDvmdxLwYAY4ZQ','Content-Type': 'application/json'},
            body: JSON.stringify(patient)
            })
        }
        await editPatient(patient)
        return {
            success: true,
            message: "Yayy!!"
        };
    }
};