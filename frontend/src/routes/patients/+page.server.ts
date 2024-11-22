export const load = async()=> {
    const getPatients = async()=>{
        const resp = await fetch('http://127.0.0.1:8000/api/patient',{headers: {Authorization:'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImU0NzIzYjJmLTEyYTktNGVkNi1iYzVmLWU3M2Y5N2E0MTZhOSIsImVtYWlsIjoidW1pQGV4YW1wbGUuY29tIiwiZXhwIjoxNzMyMjM0NTI3fQ.28u-cAh-xXzIv3OBszP0LwXhJgXgQ_7qMs-TLxIQJNI','Content-Type': 'application/json'}})
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
        const formEntries = Object.fromEntries(data.entries()); // Convert form data to an object
        let patient ={
            name: data.get("name"),
            status: parseInt(data.get("status")),
            sex: parseInt(data.get("gender")),
            birth_date: data.get("birthdate").split("/").reverse().join("-"),
            cpf: data.get("cpf")
        }
        console.log(patient); // Log form data on the server
        let id = data.get("id")
        async function editPatient(patient) {
            const response2 = fetch(`http://127.0.0.1:8000/api/patient/${id}`,{
            method: 'PUT',
            headers: {Authorization:'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImU0NzIzYjJmLTEyYTktNGVkNi1iYzVmLWU3M2Y5N2E0MTZhOSIsImVtYWlsIjoidW1pQGV4YW1wbGUuY29tIiwiZXhwIjoxNzMyMjM0NTI3fQ.28u-cAh-xXzIv3OBszP0LwXhJgXgQ_7qMs-TLxIQJNI','Content-Type': 'application/json'},
            body: JSON.stringify(patient)
            })
            console.log("paciente do server paciente")
        }
        await editPatient(patient)
        return {
            success: true,
            message: "Yay!!"
        };
    }
};